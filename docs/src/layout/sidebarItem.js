import { useState } from "react";
import { Link as RouterLink } from "react-router-dom";
import PropTypes from "prop-types";
import { ChevronDownIcon } from "../icons/chevronDown";
import { ChevronRightIcon } from "../icons/chevronRight";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Collapse from "@mui/material/Collapse";
import ListItem from "@mui/material/ListItem";

export function SidebarItem(props) {
  const {
    active,
    chip,
    children,
    depth,
    icon,
    info,
    open: openProp,
    path,
    title,
    ...other
  } = props;

  const [open, setOpen] = useState(openProp);

  const handleToggle = () => {
    setOpen((prevOpen) => !prevOpen);
  };

  let paddingLeft = 24;

  if (depth > 0) {
    paddingLeft = 32 + 8 * depth;
  }

  // Branch
  if (children) {
    return (
      <ListItem
        disableGutters
        sx={{
          display: "block",
          mb: 0.5,
          py: 0,
          px: 2,
        }}
        {...other}
      >
        <Button
          endIcon={
            !open ? (
              <ChevronRightIcon fontSize="small" />
            ) : (
              <ChevronDownIcon fontSize="small" />
            )
          }
          disableRipple
          onClick={handleToggle}
          startIcon={icon}
          sx={{
            color: active ? "secondary.main" : "text.primary",
            justifyContent: "flex-start",
            pl: `${paddingLeft}px`,
            pr: 3,
            textAlign: "left",
            textTransform: "none",
            width: "100%",
            "&:hover": {
              backgroundColor: "rgba(255,255,255, 0.08)",
            },
            "& .MuiButton-startIcon": {
              color: active ? "secondary.main" : "action.active",
            },
            "& .MuiButton-endIcon": {
              color: "action.active",
            },
          }}
        >
          <Box sx={{ flexGrow: 1 }}>{title}</Box>
          {info}
        </Button>
        <Collapse in={open} sx={{ mt: 0.5 }}>
          {children}
        </Collapse>
      </ListItem>
    );
  }

  // Leaf
  return (
    <ListItem
      disableGutters
      sx={{
        display: "flex",
        mb: 0.5,
        py: 0,
        px: 2,
      }}
    >
      <Button
        component={RouterLink}
        to={path}
        startIcon={icon}
        endIcon={chip}
        disableRipple
        sx={{
          backgroundColor: active && "rgba(255,255,255, 0.08)",
          borderRadius: 1,
          color: active ? "secondary.main" : "text.primary",
          fontWeight: active && "fontWeightBold",
          justifyContent: "flex-start",
          pl: `${paddingLeft}px`,
          pr: 3,
          textAlign: "left",
          textTransform: "none",
          width: "100%",
          "& .MuiButton-startIcon": {
            color: active ? "secondary.main" : "action.active",
          },
          "&:hover": {
            backgroundColor: "rgba(255,255,255, 0.08)",
          },
        }}
      >
        <Box sx={{ flexGrow: 1 }}>{title}</Box>
        {info}
      </Button>
    </ListItem>
  );
}

SidebarItem.propTypes = {
  active: PropTypes.bool,
  children: PropTypes.node,
  depth: PropTypes.number.isRequired,
  icon: PropTypes.node,
  info: PropTypes.node,
  open: PropTypes.bool,
  path: PropTypes.string,
  chip: PropTypes.any,
  title: PropTypes.string.isRequired,
};

SidebarItem.defaultProps = {
  active: false,
  open: false,
};
