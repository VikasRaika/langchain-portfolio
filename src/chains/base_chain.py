from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class BaseChain(BaseModel):
    """Base class for all chains in the project."""
    
    name: str
    description: str
    steps: List[str]
    config: Optional[Dict[str, Any]] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self.config = self.config or {}
    
    def initialize(self) -> None:
        """Initialize the chain with its configuration."""
        pass
    
    def run(self, input_data: Any) -> Any:
        """Run the chain's sequence of steps."""
        raise NotImplementedError("Subclasses must implement run method")
    
    def validate_input(self, input_data: Any) -> bool:
        """Validate the input data before processing."""
        return True
    
    def cleanup(self) -> None:
        """Clean up any resources used by the chain."""
        pass
