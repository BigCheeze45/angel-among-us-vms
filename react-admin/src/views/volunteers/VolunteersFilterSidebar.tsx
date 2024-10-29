import {SavedQueriesList, FilterLiveSearch, FilterList, FilterListItem} from "react-admin"
import {Card, CardContent} from "@mui/material"
import CategoryIcon from "@mui/icons-material/LocalOffer"
import BookmarkIcon from "@mui/icons-material/BookmarkBorder"
import StarBorderIcon from "@mui/icons-material/StarBorder"
import CardMembershipIcon from "@mui/icons-material/CardMembership"

export const VolunteerFilterSidebar = () => {
  return (
    // -1 display on the left rather than on the right of the list
    <Card sx={{order: -1, mr: 2, mt: 6, mb: 7, width: 200}}>
      <CardContent>
        <SavedQueriesList icon={<BookmarkIcon />} />
        <FilterLiveSearch
          source="q"
          label="Search"
        />
        <FilterList
          label="Active"
          icon={<StarBorderIcon />}
        >
          <FilterListItem
            label="Yes"
            value={{active: true}}
          />
          <FilterListItem
            label="No"
            value={{active: false}}
          />
        </FilterList>
        <FilterList
          label="Maddie certification"
          icon={<CardMembershipIcon />}
        >
          <FilterListItem
            label="Yes"
            value={{has_maddie_certifications: true}}
          />
          <FilterListItem
            label="No"
            value={{has_maddie_certifications: false}}
          />
        </FilterList>
        <FilterList
          label="Primary job"
          icon={<CategoryIcon />}
        >
          <FilterListItem
            label="Volunteer"
            value={{job_title: "AAU Volunteer"}}
          />
          <FilterListItem
            label="Team Lead"
            value={{job_title: "AAU Team Lead"}}
          />
          <FilterListItem
            label="Staff"
            value={{job_title: "AAU Staff Member"}}
          />
          <FilterListItem
            label="Officer"
            value={{job_title: "AAU Officer"}}
          />
          <FilterListItem
            label="Board Member"
            value={{job_title: "AAU Board Member"}}
          />
        </FilterList>
      </CardContent>
    </Card>
  )
}
