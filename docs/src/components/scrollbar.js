import { forwardRef } from "react";
import SimpleBar from "simplebar-react";
import { styled } from "@mui/material/styles";

import "simplebar/dist/simplebar.min.css";

const ScrollbarRoot = styled(SimpleBar)``;

export const Scrollbar = forwardRef((props, ref) => (
  <ScrollbarRoot ref={ref} {...props} />
));
