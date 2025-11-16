"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class ExtraLink(BaseModel):
    label: str = Field(..., description="Type of link, e.g., Transfermarkt")
    url: Optional[str] = Field(None, description="URL to the resource")

class Player(BaseModel):
    """
    Player submission schema
    Collection name: "player"
    """
    full_name: str = Field(..., description="Player's full name")
    age: Optional[int] = Field(None, ge=0, le=100, description="Age in years")
    country: Optional[str] = Field(None, description="Country of origin")
    position: Optional[str] = Field(None, description="Playing position")
    height: Optional[str] = Field(None, description="Height (e.g., 180 cm)")
    weight: Optional[str] = Field(None, description="Weight (e.g., 75 kg)")
    dominant_foot: Optional[str] = Field(None, description="Left or Right")
    current_club: Optional[str] = Field(None, description="Current club name")
    past_clubs: Optional[str] = Field(None, description="Past clubs (comma-separated)")
    bio: Optional[str] = Field(None, description="Short bio/about me")

    # Media
    profile_photo_base64: Optional[str] = Field(None, description="Base64-encoded profile image")
    highlight_video_base64: Optional[str] = Field(None, description="Base64-encoded highlight video (optional)")
    highlight_video_link: Optional[str] = Field(None, description="Link to highlight video (YouTube/Drive)")

    # Links
    extra_links: Optional[List[ExtraLink]] = Field(default_factory=list, description="Additional links like Transfermarkt, Instagram, etc.")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
