from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class BasePrompt(BaseModel):
    """Base class for prompt templates."""
    
    name: str
    description: str
    template: str
    input_variables: List[str]
    default_values: Dict[str, Any] = {}
    
    def __init__(self, **data):
        super().__init__(**data)
        self.default_values = self.default_values or {}
    
    def format(self, **kwargs: Any) -> str:
        """Format the prompt template with the given variables."""
        # Merge default values with provided values
        values = {**self.default_values, **kwargs}
        
        # Validate that all required variables are provided
        missing_vars = [var for var in self.input_variables if var not in values]
        if missing_vars:
            raise ValueError(f"Missing required variables: {missing_vars}")
        
        # Format the template
        try:
            return self.template.format(**values)
        except KeyError as e:
            raise ValueError(f"Invalid variable in template: {e}")
    
    def get_variables(self) -> List[str]:
        """Get all variables used in the template."""
        return self.input_variables
    
    def set_default(self, variable: str, value: Any) -> None:
        """Set a default value for a variable."""
        if variable not in self.input_variables:
            raise ValueError(f"Variable {variable} not in template variables")
        self.default_values[variable] = value
