from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class BaseMemory(BaseModel):
    """Base class for memory implementations."""
    
    name: str
    description: str
    max_history: int = 10
    memory: List[Dict[str, Any]] = []
    
    def __init__(self, **data):
        super().__init__(**data)
        self.memory = []
    
    def add(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Add a new entry to the memory."""
        entry = {
            "role": role,
            "content": content,
            "metadata": metadata or {}
        }
        self.memory.append(entry)
        if len(self.memory) > self.max_history:
            self.memory.pop(0)
    
    def get(self, n: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get the last n entries from memory."""
        if n is None:
            return self.memory
        return self.memory[-n:]
    
    def clear(self) -> None:
        """Clear all entries from memory."""
        self.memory = []
    
    def get_context(self) -> str:
        """Get the conversation context as a string."""
        return "\n".join([f"{entry['role']}: {entry['content']}" for entry in self.memory])
