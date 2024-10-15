import { SavedQueriesList, FilterLiveSearch, FilterList, FilterListItem } from 'react-admin'
import { Card, CardContent } from '@mui/material'
import MailIcon from '@mui/icons-material/MailOutline'
import CategoryIcon from '@mui/icons-material/LocalOffer'
import BookmarkIcon from '@mui/icons-material/BookmarkBorder'


export const VolunteerFilterSidebar = () => (
    // -1 display on the left rather than on the right of the list
    <Card sx={{ order: -1, mr: 2, mt: 6, mb: 7, width: 200 }}>
        <CardContent>
            <SavedQueriesList icon={<BookmarkIcon />} />
            <FilterLiveSearch source="q" label="Search" />
            <FilterList label="Active volunteer" icon={<MailIcon />}>
                <FilterListItem label="Yes" value={{ active: true }} />
                <FilterListItem label="No" value={{ active: false }} />
            </FilterList>
            <FilterList label="Maddie certification" icon={<CategoryIcon />}>
                <FilterListItem label="Yes" value={{ has_maddie_certifications: true }} />
                <FilterListItem label="No" value={{ has_maddie_certifications: false }} />
            </FilterList>
            {/* <FilterList label="Category" icon={<CategoryIcon />}>
                <FilterListItem label="Tests" value={{ category: 'tests' }} />
                <FilterListItem label="News" value={{ category: 'news' }} />
                <FilterListItem label="Deals" value={{ category: 'deals' }} />
                <FilterListItem label="Tutorials" value={{ category: 'tutorials' }} />
            </FilterList> */}
        </CardContent>
    </Card>
)
