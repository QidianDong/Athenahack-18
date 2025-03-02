import { StrictMode } from "react";
import "./index.css";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";

// biome-ignore lint/style/noNonNullAssertion: Provided by React
const rootElement = document.getElementById("root")!;
if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <StrictMode>
      <App />
    </StrictMode>,
  );
}
