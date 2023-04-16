import xml.etree.ElementTree as ET
from z3 import Not, And, Or, Bool, Solver

NAMESPACES = {
    "cddx": "http://schemas.circuit-diagram.org/circuitDiagramDocument/2012/document"
}

ELEMENT_ID = {
    "{0}": "NAND",
    "{1}": "NOR",
    "{2}": "CONN"
}


# Defined Nand and Nor just for fun lol :)
def Nand(a, b):
    return Not(And(a, b))


def Nor(a, b):
    return Not(Or(a, b))


def trace_c(c):  # Trace and attempts to solve the selected component (c)
    cns = c.findall("cddx:cns/cddx:cn", namespaces=NAMESPACES)
    if c is output:
        return trace_cn(cns[0])

    elif c in inputs:
        return Bool(str(inputs.index(c)))

    temp = []

    for cn in cns:
        if cn.attrib["pt"] != "out":
            temp.append(cn)

    c_type = ELEMENT_ID[c.attrib["tp"]]

    if c_type == "NAND":
        return Nand(trace_cn(temp[0]), trace_cn(temp[1]))
    elif c_type == "NOR":
        return Nor(trace_cn(temp[0]), trace_cn(temp[1]))


def trace_cn(cn): # Trace and attempts to solve the selected connection (cn)
    cs = connections[cn.attrib["id"]]
    if len(cs) > 1:
        return Or(*[trace_c(c) for c in cs])
    return trace_c(cs[0])


# Parse XML data
tree = ET.parse("Document.xml")
root = tree.getroot()

# Variables to store components and connections
components = root.findall("cddx:elements/cddx:c", namespaces=NAMESPACES)
output = None
inputs = []
connections = {}

# Loop through all components and add them to variables
for c in components:
    cns = c.findall("cddx:cns/cddx:cn", namespaces=NAMESPACES)
    c_type = ELEMENT_ID[c.attrib["tp"]]

    if c_type == "CONN":

        # There's more than one way to determine the output
        # One of the easier ways is to just check the x coordinates
        if c.attrib["x"] == "2690":  # OUTPUT
            output = c
        else:                        # INPUT
            inputs.append(c)
            for cn in cns:
                temp = connections.get(cn.attrib["id"], [])
                temp.append(c)
                connections[cn.attrib["id"]] = temp

    elif c_type == "NAND":           # NAND
        for cn in cns:
            if cn.attrib["pt"] == "out":
                temp = connections.get(cn.attrib["id"], [])
                temp.append(c)
                connections[cn.attrib["id"]] = temp

    elif c_type == "NOR":            # NOR
        for cn in cns:
            if cn.attrib["pt"] == "out":
                temp = connections.get(cn.attrib["id"], [])
                temp.append(c)
                connections[cn.attrib["id"]] = temp


# Sort inputs by their y coordinate
# Important cause input components' "id" attributes are not in order
inputs.sort(key=lambda c: int(c.attrib["y"]))


# Trace entire circuit starting from output
circuit = trace_c(output)

# from z3 import solve
# solve(circuit)

# Solve the circuit using z3
s = Solver()
s.add(circuit)
r = s.check()

# Formatting the flag
model = s.model()
decls = model.decls()
decls.sort(key=lambda x: int(str(x)))
results = ["01"[bool(model.get_interp(i))] for i in decls]
flag = "LNC2023{" + "".join(results) + "}"

print(flag)  # LNC2023{10111000101101000100010110000110}
