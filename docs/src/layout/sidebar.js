import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import PropTypes from "prop-types";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import useMediaQuery from "@mui/material/useMediaQuery";
import { SidebarSection } from "./sidebarSection";
import { Scrollbar } from "../components/scrollbar";

const sections = [
  {
    title: "overview",
    items: [
      {
        title: "Welcome",
        path: "/welcome",
      },
      {
        title: "Code of Conduct",
        path: "/codeOfConduct",
      },
      {
        title: "Contributing",
        path: "/contributingGuide",
      },
      {
        title: "Security",
        path: "/securityGuide",
      },
      {
        title: "MIT License",
        path: "/mitLicense",
      },
    ],
  },
  {
    title: "packages",
    items: [
      {
        title: "iot-edge-logger",
        path: "/packages/iotEdgeLogger",
      },
      {
        title: "iot-edge-validator",
        path: "/packages/iotEdgeValidator",
      },
      {
        title: "iot-ftps-client",
        path: "/packages/iotFtpsClient",
      },
      {
        title: "iot-lru-cache",
        path: "/packages/iotLruCache",
      },
      {
        title: "iot-samba-client",
        path: "/packages/iotSambaClient",
      },
      {
        title: "iot-storage-client",
        children: [
          {
            title: "Asynchronous Client",
            path: "/packages/iotStorageClientAsync",
          },
          {
            title: "Synchronous Client",
            path: "/packages/iotStorageClient",
          },
        ],
      },
    ],
  },
  {
    title: "changelog",
    items: [
      {
        title: "iot-edge-logger",
        path: "/changelog/iotEdgeLogger",
      },
      {
        title: "iot-edge-validator",
        path: "/changelog/iotEdgeValidator",
      },
      {
        title: "iot-ftps-client",
        path: "/changelog/iotFtpsClient",
      },
      {
        title: "iot-samba-client",
        path: "/changelog/iotSambaClient",
      },
      {
        title: "iot-storage-client",
        path: "/changelog/iotStorageClient",
      },
    ],
  },
];

export function Sidebar(props) {
  const { onClose, open } = props;
  const location = useLocation();
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up("lg"));

  useEffect(() => {
    if (open && onClose) {
      onClose();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [location.pathname]);

  const content = (
    <Scrollbar
      sx={{
        height: "100%",
        "& .simplebar-content": {
          height: "100%",
        },
      }}
    >
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          height: "100%",
          py: 2,
        }}
      >
        {sections.map((section) => (
          <SidebarSection
            key={section.title}
            path={location.pathname}
            sx={{
              "& + &": {
                mt: 3,
              },
            }}
            {...section}
          />
        ))}
      </Box>
    </Scrollbar>
  );

  if (lgUp) {
    return (
      <Drawer
        anchor="left"
        open
        variant="permanent"
        PaperProps={{
          sx: {
            backgroundColor: "background.paper",
            height: "calc(100% - 64px) !important",
            top: "64px !important",
            width: 256,
          },
        }}
      >
        {content}
      </Drawer>
    );
  }

  return (
    <Drawer
      anchor="right"
      onClose={onClose}
      open={open}
      variant="temporary"
      PaperProps={{
        sx: {
          backgroundColor: "background.default",
          width: 256,
        },
      }}
      sx={{
        zIndex: (theme) => theme.zIndex.appBar + 100,
      }}
    >
      {content}
    </Drawer>
  );
}

Sidebar.propTypes = {
  onClose: PropTypes.func,
  open: PropTypes.bool,
};
