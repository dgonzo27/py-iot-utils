// lazy loading
import { Suspense, lazy } from "react";
import { Navigate } from "react-router-dom";
import { Layout } from "./layout/layout";
import { Spinner } from "./components/spinner";

const Loadable = (Component) =>
  function (props) {
    return (
      <Suspense fallback={<Spinner />}>
        <Component {...props} />
      </Suspense>
    );
  };

// pages
const Docs = Loadable(lazy(() => import("./pages/docs")));

const routes = [
  {
    path: "",
    element: <Layout />,
    children: [
      { path: "", element: <Navigate to="/welcome" replace /> },
      { path: "*", element: <Docs /> },
    ],
  },
];

export default routes;
