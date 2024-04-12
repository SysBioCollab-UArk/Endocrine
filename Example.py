from pysb import *
from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

Model()

Monomer("A", ["b"])
Monomer("B", ["a"])

Parameter("A_0", 90)
Parameter("B_0", 100)

Initial(A(b=None), A_0)
Initial(B(a=None), B_0)

Parameter("Kf_ab", 1)
Parameter("Kr_ab", 10)

Rule("A_binds_B", A(b=None) + B(a=None) | A(b=1) % B(a=1),Kf_ab,Kr_ab,)

Observable("A_free", A(b=None))
Observable("B_free", B(a=None))
Observable("AB_complex",  A(b=1) % B(a=1))

print(model)

tspan= np.linspace(0,0.1,101)
Sim= ScipyOdeSimulator(model,tspan,verbose=True)

out=Sim.run()

for obs in model.observables:
    plt.plot(tspan, out.observables[obs.name], lw=2, label=obs.name)
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend(loc=0)
plt.tight_layout()

plt.show()
