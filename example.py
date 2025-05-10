from src.bloqade.hamiltonian.types import HamiltonianOperator, TimeEvolution
from src.bloqade.hamiltonian.simulation import create_simulator
from src.bloqade.types import QubitType
from typing import Optional

def simulate_quantum_system():
    """Example of simulating a quantum system using the Hamiltonian package."""
    
    # 1. Define the system
    hamiltonian = HamiltonianOperator(
        qubits=[0, 1],  # Two qubits
        parameters={
            "J": 1.0,  # ZZ coupling strength
            "h": 0.5   # Field strength
        }
    )
    
    # 2. Define the evolution
    evolution = TimeEvolution(
        hamiltonian=hamiltonian,
        time=1.0  # Evolve for 1 unit of time
    )
    
    # 3. Create simulator
    simulator = create_simulator(
        method="partial_trotter",
        order=2,  # Second-order Trotter
        steps=100,  # Number of time steps
        radius=3
    )
    
    # 5. Run simulation
    final_operator = simulator.simulate(
        evolution=evolution
    )

if __name__ == "__main__":
    import os
    print(f"Current execution path: {os.getcwd()}")
    simulate_quantum_system()