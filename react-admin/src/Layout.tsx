import Menu from "./components/Menu"
import type {ReactNode} from "react"
import {Layout as RALayout, CheckForApplicationUpdate} from "react-admin"

export const Layout = ({children}: {children: ReactNode}) => (
  <RALayout menu={Menu}>
    {children}
    <CheckForApplicationUpdate />
  </RALayout>
)
