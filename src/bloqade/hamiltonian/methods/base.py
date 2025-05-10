# src/bloqade/hamiltonian/methods/base.py
from abc import ABC, abstractmethod
from typing import Optional, List, Callable, Protocol
from bloqade.types import QubitType
from bloqade.hamiltonian.types import TimeEvolution, HamiltonianOperator
from bloqade import qasm2

class SimulationMethod(ABC):
    """Base class for Hamiltonian simulation methods."""
    
    @abstractmethod
    def decompose_hamiltonian(self, hamiltonian: HamiltonianOperator) -> List[HamiltonianOperator]:
        """Decompose a Hamiltonian into terms for simulation.
        
        Args:
            hamiltonian: The Hamiltonian to decompose
            
        Returns:
            List of Hamiltonian terms
        """
        pass
    
    @abstractmethod
    def simulate(
        self,
        evolution: TimeEvolution,
        **kwargs
    ) -> qasm2.Method:
        """Simulate the evolution of a quantum state under a Hamiltonian.
        
        Args:
            evolution: The time evolution to simulate
            **kwargs: Additional simulation parameters
            
        Returns:
            A QASM circuit object that implements the Hamiltonian evolution.
            This circuit can be optimized by Bloqade's circuit compiler.
        """
        pass