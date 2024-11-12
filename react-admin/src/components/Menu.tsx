import {Menu as RAMenu} from "react-admin"
import {Box, useTheme} from "@mui/material"

const Menu = () => {
  const theme = useTheme()
  const isDarkMode = theme.palette.mode === "dark"

  return (
    <Box
      sx={{
        width: 300,
        marginRight: -9.5,
        padding: 1,
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-start",
        backgroundColor: isDarkMode ? "#333" : "#bcd8ed",
        boxShadow: isDarkMode ? "0px 4px 12px rgba(255, 255, 255, 0.1)" : "0px 4px 12px rgba(0, 0, 0, 0.1)",
      }}
    >
      <Box
        sx={{
          width: "40px", // Increased circle size
          height: "40px", // Increased circle size
          borderRadius: "50%", // Ensure the container remains circular
          border: isDarkMode ? "1px solid #7d7e82" : "1px solid #b1b2b4",
          backgroundColor: isDarkMode ? "#333" : "#f0f0f0", // Background color for circle
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          marginLeft: "5px",
        }}
      >
        <img
          src="/favicon.png"
          alt="Logo"
          style={{
            width: "23px",
            height: "23px",
          }}
        />
      </Box>

      {/* Separator line */}
      <Box
        component="hr"
        sx={{
          width: "100%",
          border: "none",
          borderTop: `1px solid ${isDarkMode ? "#7d7e82" : "#b1b2b4"}`,
        }}
      />

      <RAMenu
        sx={{
          "& .RaMenuItem": {
            color: isDarkMode ? "#fff" : "#333", // Text color based on theme
            padding: "8px 16px",
            fontWeight: "bold",
            "&:hover": {
              backgroundColor: isDarkMode ? "#444" : "#e0f7fa", // Hover color for both themes
            },
          },
        }}
      />
    </Box>
  )
}

export default Menu
