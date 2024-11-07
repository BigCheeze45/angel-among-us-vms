import {Login} from "react-admin"
import {OneTapButton} from "ra-auth-google"
import {LoginButton} from "../components/LoginButton"

export const LoginPage = () => {
  return (
    <OneTapButton>
      <Login
        style={{
          // teletubbies sun
          // backgroundImage: 'radial-gradient(#ffcf25 10px, #ffde73 30%, #57a0d5 50%)'
          // Blue flames
          backgroundImage: "radial-gradient(circle at 50% 14em, #ffcf25 0%, #ffde73 20%, #57a0d5 100%)",
        }}
      >
        <LoginButton
          shape="pill"
          width="300"
          theme="outline"
        />
      </Login>
    </OneTapButton>
  )
}
