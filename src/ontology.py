from pydantic import BaseModel, Field
from typing import List, Optional

class ExtractedClaim(BaseModel):
    """A single fact extracted from an email with identity normalization."""
    
    raw_subject: str = Field(
        description="The name exactly as it appears in the text."
    )
    canonical_subject: Optional[str] = Field(
        description="Normalized full name guess based on context."
    )
    normalization_confidence: float = Field(
        description="How sure are you about this name mapping? (0.0 to 1.0)"
    )
    predicate: str = Field(
        description="The action or relationship (e.g., 'WORKS_ON', 'APPROVED')."
    )
    object_name: str = Field(
        description="The entity or value the subject is linked to."
    )
    excerpt: str = Field(
        description="The EXACT verbatim text from the email as evidence. Do not paraphrase."
    )

class ExtractionSchema(BaseModel):
    """The full output from the LLM for one email."""
    claims: List[ExtractedClaim]