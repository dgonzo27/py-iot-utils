import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Helmet } from "react-helmet-async";
import ReactMarkdown from "react-markdown";
import * as matter from "gray-matter";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { materialOceanic } from "react-syntax-highlighter/dist/esm/styles/prism";
import Container from "@mui/material/Container";
import { styled } from "@mui/material/styles";

const MarkdownWrapper = styled("div")(({ theme }) => ({
  color: theme.palette.text.primary,
  fontFamily: theme.typography.fontFamily,
  "& blockquote": {
    borderLeft: `4px solid ${theme.palette.text.secondary}`,
    marginBottom: theme.spacing(2),
    paddingBottom: theme.spacing(1),
    paddingLeft: theme.spacing(2),
    paddingTop: theme.spacing(1),
    "& > p": {
      color: theme.palette.text.secondary,
      marginBottom: 0,
    },
  },
  "& code": {
    color: "#01ab56",
    fontFamily:
      'Inconsolata, Monaco, Consolas, "Courier New", Courier, monospace',
    fontSize: 14,
    paddingLeft: 2,
    paddingRight: 2,
  },
  "& h1": {
    fontSize: 35,
    fontWeight: 500,
    letterSpacing: "-0.24px",
    marginBottom: theme.spacing(2),
    marginTop: theme.spacing(6),
  },
  "& h2": {
    fontSize: 29,
    fontWeight: 500,
    letterSpacing: "-0.24px",
    marginBottom: theme.spacing(2),
    marginTop: theme.spacing(6),
  },
  "& h3": {
    fontSize: 24,
    fontWeight: 500,
    letterSpacing: "-0.06px",
    marginBottom: theme.spacing(2),
    marginTop: theme.spacing(6),
  },
  "& h4": {
    fontSize: 20,
    fontWeight: 500,
    letterSpacing: "-0.06px",
    marginBottom: theme.spacing(2),
    marginTop: theme.spacing(4),
  },
  "& h5": {
    fontSize: 16,
    fontWeight: 500,
    letterSpacing: "-0.05px",
    marginBottom: theme.spacing(2),
    marginTop: theme.spacing(2),
  },
  "& h6": {
    fontSize: 14,
    fontWeight: 500,
    letterSpacing: "-0.05px",
    marginBottom: theme.spacing(2),
    marginTop: theme.spacing(2),
  },
  "& li": {
    fontSize: 14,
    lineHeight: 1.5,
    marginBottom: theme.spacing(2),
    marginLeft: theme.spacing(4),
  },
  "& p": {
    fontSize: 14,
    lineHeight: 1.5,
    marginBottom: theme.spacing(2),
    "& > a": {
      color: theme.palette.secondary.main,
    },
  },
}));

function Docs() {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const [file, setFile] = useState(null);

  useEffect(() => {
    const getFile = async () => {
      try {
        const response = await fetch(`/static${pathname}.md`, {
          headers: {
            accept: "text/markdown",
          },
        });

        if (response.status !== 200) {
          navigate("/500", { replace: true });
          return;
        }

        const data = await response.text();

        setFile(matter(data));
      } catch (err) {
        console.error(err);
        navigate("/500");
      }
    };
    getFile();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pathname, navigate]);

  if (!file) {
    return null;
  }

  return (
    <div>
      <Helmet>
        <title>{`Docs: ${file.data.title} | py-iot-utils`}</title>
      </Helmet>
      <Container maxWidth="lg" sx={{ pb: "120px" }}>
        <MarkdownWrapper>
          <ReactMarkdown
            children={file.content}
            components={{
              code({ node, inline, className, children, ...props }) {
                const match = /language-(\w+)/.exec(className || "");
                return !inline && match ? (
                  <SyntaxHighlighter
                    children={String(children).replace(/\n$/, "")}
                    style={materialOceanic}
                    language={match[1]}
                    PreTag="div"
                    {...props}
                  />
                ) : (
                  <code className={className} {...props}>
                    {children}
                  </code>
                );
              },
            }}
          />
        </MarkdownWrapper>
      </Container>
    </div>
  );
}

export default Docs;
