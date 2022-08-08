import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import GitHubIcon from "@mui/icons-material/GitHub";
import { PyPiIcon } from "../icons/pypi";

export const Footer = () => {
  const links = [
    {
      id: 1,
      marginRight: 2,
      link: "https://github.com/dgonzo27/py-iot-utils",
      icon: <GitHubIcon color="primary" />,
    },
    {
      id: 2,
      link: "https://pypi.org/user/dgonzo27/",
      icon: <PyPiIcon color="primary" />,
    },
  ];

  return (
    <Container maxWidth="lg" sx={{ pt: 4, pb: 2 }}>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            width={1}
            flexDirection={{ xs: "column", sm: "row" }}
          >
            <Box>
              <Typography
                variant="subtitle2"
                color="text.secondary"
                align="center"
                gutterBottom
              >
                &copy;2022 py-iot-utils. All rights reserved.
              </Typography>
            </Box>

            <Box display="flex" flexWrap="wrap" alignItems="center">
              {links.map((l) => (
                <Box
                  key={l.id}
                  marginTop={1}
                  marginRight={l.marginRight}
                  component="a"
                  href={l.link}
                  target="_blank"
                  rel="no-referrer"
                >
                  {l.icon}
                </Box>
              ))}
            </Box>
          </Box>
        </Grid>
      </Grid>
    </Container>
  );
};
