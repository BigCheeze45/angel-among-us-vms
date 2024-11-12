import {createTheme} from "@mui/material/styles"
import {RaThemeOptions} from "react-admin"

const lightTheme: RaThemeOptions = createTheme({
  palette: {
    mode: "light",
    primary: {main: "#2970a3"},
    secondary: {main: "#ffcf25"},
    background: {default: "#bcd8ed"},
    text: {primary: "#0d0d0d", secondary: "#7d7e82"},
  },

  typography: {
    h6: {fontWeight: 700},
  },

  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          boxShadow: "0px 4px 12px rgba(0, 0, 0, 0.1)",
          borderRadius: "12px",
          padding: "3px",
          transition: "background-color 0.3s ease, color 0.3s ease",
        },
      },
    },
  },
})

const darkTheme: RaThemeOptions = createTheme({
  palette: {
    mode: "dark",
    primary: {main: "#90caf9"},
    secondary: {main: "#ffcf25"},
    background: {default: "#303030"},
    text: {primary: "#ffffff", secondary: "#b0bec5"},
  },
  typography: {
    h6: {fontWeight: 700},
  },
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          boxShadow: "0px 4px 12px rgba(0, 0, 0, 0.3)",
          borderRadius: "12px",
          padding: "3px",
          transition: "background-color 0.3s ease, color 0.3s ease",
        },
      },
    },
  },
})

export {lightTheme, darkTheme}
