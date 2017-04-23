%typeset_mode True
A = ([-1, 1], [1, 0], [0,1])
b = (1,3,2)
c = (1,1)
P = InteractiveLPProblemStandardForm(A, b, c, ["x1", "x2"])
P.plot()
view(P)
D = P.initial_dictionary()
view(D)
