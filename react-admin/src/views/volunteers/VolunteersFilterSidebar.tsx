import {Card, CardContent} from "@mui/material"
import LoyaltyIcon from "@mui/icons-material/Loyalty"
import {subYears, format, startOfYear} from "date-fns"
import CategoryIcon from "@mui/icons-material/LocalOffer"
import StarBorderIcon from "@mui/icons-material/StarBorder"
import CardMembershipIcon from "@mui/icons-material/CardMembership"
import {SavedQueriesList, FilterLiveSearch, FilterList, FilterListItem} from "react-admin"

export const VolunteerFilterSidebar = () => {
  return (
    // -1 display on the left rather than on the right of the list
    <Card sx={{order: -1, mr: 2, mt: 6, mb: 7, width: 200}}>
      <CardContent>
        <SavedQueriesList />
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
            value={{has_maddie_certification: false}}
          />
          <FilterListItem
            label="No"
            value={{has_maddie_certification: true}}
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
        <FilterList
          label="Years of service"
          icon={<LoyaltyIcon />}
        >
          <FilterListItem
            label="1 or less"
            value={{
              date_joined_after: format(startOfYear(new Date()), "yyyy-dd-MM"),
            }}
          />
          <FilterListItem
            label="3+"
            value={{
              date_joined_before: format(startOfYear(new Date()), "yyyy-dd-MM"),
              date_joined_after: format(subYears(startOfYear(new Date()), 3), "yyyy-dd-MM"),
            }}
          />
          <FilterListItem
            label="5+"
            value={{
              date_joined_before: format(startOfYear(new Date()), "yyyy-dd-MM"),
              date_joined_after: format(subYears(startOfYear(new Date()), 5), "yyyy-dd-MM"),
            }}
          />
          <FilterListItem
            label="10+"
            value={{
              date_joined_before: format(startOfYear(new Date()), "yyyy-dd-MM"),
              date_joined_after: format(subYears(startOfYear(new Date()), 10), "yyyy-dd-MM"),
            }}
          />
        </FilterList>
      </CardContent>
    </Card>
  )
}
