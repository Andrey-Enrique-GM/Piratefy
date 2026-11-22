from dataclasses import dataclass
from typing import Optional



@dataclass
class PlaylistCancion:
    playlist_id: int
    cancion_id: int
    id: Optional[int] = None


    @classmethod
    def from_row(cls, row: dict) -> "PlaylistCancion":
        return cls(
            id=row.get("id"),
            playlist_id=row["playlist_id"],
            cancion_id=row["cancion_id"],
        )


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "playlist_id": self.playlist_id,
            "cancion_id": self.cancion_id,
        }
    