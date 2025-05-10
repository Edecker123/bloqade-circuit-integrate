from dataclasses import dataclass
from typing import Protocol, TypeVar, Optional
from src.bloqade.types import QubitType

#defining the expressions that contract what the hamiltonian expressions will be 
T = TypeVar('T')

@dataclass
class HamiltonianOperator:
    """Base class for Hamiltonian operators."""
    qubits: list[QubitType]
    parameters: dict[str, float]

@dataclass
class TimeEvolution:
    """Represents time evolution under a Hamiltonian."""
    hamiltonian: HamiltonianOperator
    time: float