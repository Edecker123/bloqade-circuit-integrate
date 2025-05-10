# main simulation interface 

from typing import Protocol, Callable
from .types import TimeEvolution
from .methods.trotter import TrotterSimulator, PartialTrotterSimulator
from .methods.base import SimulationMethod       

def create_simulator(method: str = "trotter", **kwargs) -> SimulationMethod:
    """Create a Hamiltonian simulator with the specified method.
    
    Args:
        method: The simulation method to use. Currently supported:
            - "trotter": Standard Trotter-Suzuki decomposition
            - "partial_trotter": Partial Trotter decomposition
        **kwargs: Additional parameters for the simulator:
            - For "trotter":
                - order: Order of Trotter-Suzuki decomposition (default: 1)
                - steps: Number of time steps (default: 100)
            - For "partial_trotter":
                - exact_terms: List of terms to treat exactly
                - order: Order for approximate terms (default: 1)
                - steps: Number of time steps (default: 100)
    
    Returns:
        A simulator instance implementing the HamiltonianSimulator protocol
    
    Raises:
        ValueError: If an unknown simulation method is specified
    """
    if method == "trotter":
        return TrotterSimulator(**kwargs)
    elif method == "partial_trotter":
        if "radius" not in kwargs:
            raise ValueError("exact_terms must be specified for partial_trotter method")
        return PartialTrotterSimulator(**kwargs)
    else:
        raise ValueError(f"Unknown simulation method: {method}")