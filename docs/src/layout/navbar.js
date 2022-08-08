import { Link as RouterLink } from "react-router-dom";
import PropTypes from "prop-types";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import Toolbar from "@mui/material/Toolbar";
import { MenuIcon } from "../icons/menu";
import { Logo } from "../components/logo";

export function Navbar({ onOpenSidebar }) {
  return (
    <AppBar
      elevation={0}
      sx={{
        backgroundColor: "background.paper",
        borderBottomColor: "divider",
        borderBottomStyle: "solid",
        borderBottomWidth: 1,
        color: "text.secondary",
      }}
    >
      <Toolbar sx={{ height: 72 }}>
        <RouterLink to="/">
          <Logo sx={{ height: 40, width: 40 }} />
        </RouterLink>
        <Box sx={{ flexGrow: 1 }} />
        <IconButton
          color="inherit"
          onClick={onOpenSidebar}
          sx={{
            display: {
              md: "none",
            },
          }}
        >
          <MenuIcon fontSize="small" />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
}

Navbar.propTypes = {
  onOpenSidebar: PropTypes.func,
};
