from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class BaseAgent(BaseModel):
    """Base class for all agents in the project."""
    
    name: str
    description: str
    capabilities: List[str]
    config: Optional[Dict[str, Any]] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self.config = self.config or {}
    
    def initialize(self) -> None:
        """Initialize the agent with its configuration."""
        pass
    
    def execute(self, input_data: Any) -> Any:
        """Execute the agent's main functionality."""
        raise NotImplementedError("Subclasses must implement execute method")
    
    def cleanup(self) -> None:
        """Clean up any resources used by the agent."""
        pass
