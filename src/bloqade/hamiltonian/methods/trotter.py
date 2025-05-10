from dataclasses import dataclass
from typing import List, Callable
from bloqade.hamiltonian.types import TimeEvolution, HamiltonianOperator
from bloqade.hamiltonian.methods.base import SimulationMethod
from bloqade.squin import kernel
from bloqade.squin.qubit import new, apply
from bloqade.squin.op import x, y, z, rot

@dataclass
class TrotterSimulator(SimulationMethod):
    """Trotter simulation method for Hamiltonian evolution.
    
    This implements the standard Trotter-Suzuki decomposition for simulating
    time evolution under a Hamiltonian.
    """
    
    order: int = 1  # Order of the Trotter-Suzuki decomposition
    steps: int = 100  # Number of Trotter steps
    
    def decompose_hamiltonian(self, hamiltonian: HamiltonianOperator) -> List[HamiltonianOperator]:
        """Decompose Hamiltonian into terms for Trotter simulation.
        
        For Trotter simulation, we treat each term in the Hamiltonian separately.
        """
        return hamiltonian.terms
    
    
    def simulate(
        self,
        evolution: TimeEvolution,
        **kwargs
    ) -> Callable:
        """Simulate the evolution of a quantum state under a Hamiltonian.
        
        Args:
            evolution: The time evolution to simulate
            initial_state: Optional initial state
            **kwargs: Additional parameters
            
        Returns:
            A circuit-level function that implements the Trotter decomposition
            of the Hamiltonian evolution.
        """
        pass

@dataclass
class PartialTrotterSimulator(SimulationMethod):
    """Partial Trotter simulation method for Hamiltonian evolution.
    
    This implements a partial Trotter decomposition where some terms
    are treated exactly while others use Trotter approximation.
    """
    
    radius:int  # Names of terms to treat exactly
    order: int = 1  # Order of Trotter-Suzuki for approximate terms
    steps: int = 100  # Number of Trotter steps
    
    def decompose_hamiltonian(self, hamiltonian: HamiltonianOperator) -> List[HamiltonianOperator]:
        """Decompose Hamiltonian into exact and approximate terms."""
        pass

    def simulate(
        self,
        evolution: TimeEvolution,
        **kwargs
    ) -> Callable:
        print("simulation through parital trotterization") 