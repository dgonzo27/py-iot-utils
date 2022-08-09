import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { createTheme } from "./theme";
import { useRoutes } from "react-router-dom";
import useScrollReset from "./hooks/useScrollReset";
import routes from "./routes";

function App() {
  const content = useRoutes(routes);

  useScrollReset();

  return (
    <ThemeProvider theme={createTheme()}>
      <CssBaseline />
      {content}
    </ThemeProvider>
  );
}

export default App;
