import { useState } from "react";
import { Outlet } from "react-router-dom";
import { styled } from "@mui/material/styles";
import { Footer } from "./footer";
import { Navbar } from "./navbar";
import { Sidebar } from "./sidebar";

const LayoutWrapper = styled("div")(({ theme }) => ({
  backgroundColor: theme.palette.background.paper,
  display: "flex",
  height: "100%",
  overflow: "hidden",
  paddingTop: 72,
  [theme.breakpoints.up("lg")]: {
    paddingLeft: 256,
  },
}));

const LayoutContainer = styled("div")({
  flex: "1 1 auto",
  overflow: "auto",
});

export function Layout() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  return (
    <>
      <Navbar onOpenSidebar={() => setIsSidebarOpen(true)} />
      <Sidebar onClose={() => setIsSidebarOpen(false)} open={isSidebarOpen} />
      <LayoutWrapper>
        <LayoutContainer>
          <Outlet />
          <Footer />
        </LayoutContainer>
      </LayoutWrapper>
    </>
  );
}
