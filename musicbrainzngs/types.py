from enum import Enum
from typing import List, Literal, Optional, TypedDict

JobType = Enum(
    "JobType", ["fetch_artists", "fetch_artist_videos", "find_video_sources"]
)

type RELATABLE_TYPES = Literal[
    "area",
    "artist",
    "label",
    "place",
    "event",
    "recording",
    "release",
    "release-group",
    "series",
    "url",
    "work",
    "instrument",
]

type RELATION_INCLUDES = Literal[
    "area-rels",
    "artist-rels",
    "label-rels",
    "place-rels",
    "event-rels",
    "recording-rels",
    "release-rels",
    "release-group-rels",
    "series-rels",
    "url-rels",
    "work-rels",
    "instrument-rels",
]

type TAG_INCLUDES = Literal["tags", "user-tags", "genres", "user-genres"]

type ValidReleaseStatuses = Literal[
    "official", "promotion", "bootleg", "pseudo-release"
]

type ValidReleaseTypes = Literal[
    "nat",
    "album",
    "single",
    "ep",
    "broadcast",
    "other", 
    "compilation",
    "soundtrack",
    "spokenword",
    "interview",
    "audiobook",
    "live",
    "remix",
    "dj-mix",
    "mixtape/street",
    "audio drama", 
]

type ValidAreaTypes = Literal["country", "subdivision", "county", "municipality", "city", "district", "island"]


type ArtistType = Literal["person", "group", "orchestra", "choir", "character", "other"]


class RATING_INCLUDES(Enum):
    RATINGS = "ratings"
    USER_RATINGS = "user-ratings"


type AreaIncludes = List[
    Literal["aliases"] | Literal["annotation"] | TAG_INCLUDES | RELATION_INCLUDES
]


class LifeSpan(TypedDict):
    ended: Optional[bool]
    begin: Optional[str]
    end: Optional[str]

class Area(TypedDict):
    type_id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    disambiguation: Optional[str]
    id: Optional[str]
    sort_name: Optional[str]
    life_span: Optional[LifeSpan]
    

class Artist(TypedDict):
    life_span: Optional[LifeSpan]
    sort_name: Optional[str]
    gender: Optional[Literal["male", "female", "other"]]
    ipis: Optional[List[str]]
    name: Optional[str]
    end_area: Optional[Area]
    gender_id: Optional[str]
    begin_area: Optional[Area]
    type: Optional[ArtistType]
    area: Optional[Area]
    country: Optional[str]
    type_id: Optional[str]
    disambiguation: Optional[str]
    isnis: Optional[List[str]]
    id: Optional[str]
    
    start_area: Optional[Area]
    


