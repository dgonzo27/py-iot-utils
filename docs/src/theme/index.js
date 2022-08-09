import {
  createTheme as createMuiTheme,
  responsiveFontSizes,
} from "@mui/material/styles";
import { baseTheme } from "./baseTheme";
import { customTheme } from "./customTheme";

export const createTheme = () => {
  let theme = createMuiTheme(baseTheme, customTheme);
  theme = responsiveFontSizes(theme);
  return theme;
};
