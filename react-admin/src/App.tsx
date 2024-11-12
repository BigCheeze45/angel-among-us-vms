<<<<<<< Updated upstream
import {Layout} from "./Layout"
import {LoginPage} from "./pages/Login"
import dataProvider from "./dataProvider"
import authProvider from "./authProvider"
import {Admin, Resource} from "react-admin"
import {GOOGLE_CLIENT_ID} from "./constants"
import {TeamShow} from "./views/teams/TeamShow"
import {UsersList} from "./views/users/UserList"
import {TeamList} from "./views/teams/TeamsList"
import {VolunteersList} from "./views/volunteers/VolunteersList"
import {VolunteerEdit} from "./views/volunteers/edit/VolunteerEdit"
import {VolunteerShow} from "./views/volunteers/show/VolunteerShow"
import {useGoogleAuthProvider, GoogleAuthContextProvider, localStorageTokenStore} from "ra-auth-google"

export const App = () => {
  // configure Sign-in with Google
  // Only one auto re-authn request can be made every 10 minutes.
  const {gsiParams, authProvider: googleAuthProvider} = useGoogleAuthProvider({
    auto_select: true,
    itp_support: true,
    use_fedcm_for_prompt: true,
    client_id: GOOGLE_CLIENT_ID,
    cancel_on_tap_outside: false,
    tokenStore: localStorageTokenStore,
  })
  const drfDataProvider = dataProvider()
  // wrap out auth provider around Google's, making sure to provide they're using
  // the same token store
  const drfAuthProvider = authProvider(googleAuthProvider, localStorageTokenStore)

  return (
    <GoogleAuthContextProvider value={gsiParams}>
      <Admin
        // https://marmelab.com/react-admin/Admin.html#requireauth
        requireAuth
        layout={Layout}
        loginPage={LoginPage}
        dataProvider={drfDataProvider}
        authProvider={drfAuthProvider}
      >
        <Resource
          name="volunteers"
          show={VolunteerShow}
          list={VolunteersList}
          edit={VolunteerEdit}
          hasCreate={false}
          recordRepresentation={record => `${record.full_name}`}
        />
        <Resource
          name="teams"
          list={TeamList}
          show={TeamShow}
          hasEdit={false}
          hasCreate={false}
        />
        <Resource
          name="users"
          list={UsersList}
          /*
            There is a Create view however it's a dialog that's only available
            from UsersList. Setting this to false so RA doesn't doesn't
            do anything unexpected (e.g. trying to navigate to it)
          */
          hasCreate={false}
          hasShow={false}
          hasEdit={false}
          // display user full name when presenting a record (e.g. show view)
          recordRepresentation={record => `${record.first_name} ${record.last_name}`}
        />
      </Admin>
    </GoogleAuthContextProvider>
  )
}
=======
import { Admin, Resource } from 'react-admin';
import PeopleIcon from '@mui/icons-material/People';
import PersonIcon from '@mui/icons-material/Person';
import VolunteerActivismIcon from '@mui/icons-material/VolunteerActivism';
import { Layout } from "./Layout";
import { LoginPage } from "./pages/Login";
import dataProvider from "./dataProvider";
import { lightTheme, darkTheme } from './theme';
import { TeamShow } from "./views/teams/TeamShow";
import { UserShow } from "./views/users/UserShow";
import { UsersList } from "./views/users/UserList";
import { UserEdit } from "./views/users/UserEdit";
import { TeamList } from "./views/teams/TeamsList";
import { UserCreate } from "./views/users/UserCreate";
import { VolunteerShow } from "./views/volunteers/VolunteerShow";
import { VolunteersList } from "./views/volunteers/VolunteersList";
import { useGoogleAuthProvider, GoogleAuthContextProvider } from "ra-auth-google";
import { useState } from 'react';

export const App = () => {
    const [isDarkMode, setIsDarkMode] = useState(false);
    const drfProvider = dataProvider();
    const { authProvider, gsiParams } = useGoogleAuthProvider({
        client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
    });

    const toggleTheme = () => setIsDarkMode((prevMode) => !prevMode);

    return (
        <GoogleAuthContextProvider value={gsiParams}>
            <Admin
                theme={isDarkMode ? darkTheme : lightTheme}
                requireAuth
                layout={(props) => (
                    <Layout 
                        {...props} 
                        toggleTheme={toggleTheme} 
                        isDarkMode={isDarkMode} 
                    />
                )}
                loginPage={LoginPage}
                dataProvider={drfProvider}
                authProvider={authProvider}
            >
                <Resource
                    name="volunteers"
                    show={VolunteerShow}
                    list={VolunteersList}
                    hasEdit={false}
                    hasCreate={false}
                    recordRepresentation={(record) => `${record.full_name}`}
                    icon={VolunteerActivismIcon} 
                />
                <Resource
                    name="teams"
                    list={TeamList}
                    show={TeamShow}
                    hasEdit={false}
                    hasCreate={false}
                    icon={PeopleIcon} 
                />
                <Resource
                    name="users"
                    show={UserShow}
                    edit={UserEdit}
                    list={UsersList}
                    create={UserCreate}
                    recordRepresentation={(record) => `${record.first_name} ${record.last_name}`}
                    icon={PersonIcon} 
                />
            </Admin>
        </GoogleAuthContextProvider>
    );
};

export default App;
>>>>>>> Stashed changes
