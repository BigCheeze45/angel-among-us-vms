import * as React from "react"
import {Box, SxProps, styled} from "@mui/material"
import {useLogin, useNotify} from "react-admin"
import {useGoogleAuthContext, GsiButtonConfiguration} from "ra-auth-google"

const GoogleButton = (props: Omit<LoginButtonProps, "sx">) => {
  const gsiParams = useGoogleAuthContext()
  if (!gsiParams) {
    throw new Error("LoginButton must be used inside a GoogleAuthContextProvider")
  }
  const login = useLogin()
  const notify = useNotify()
  const divRef = React.useRef<HTMLDivElement>(null)

  // eslint-disable-next-line
  const handleLogin = params => {
    login(params).catch(error => {
      // autoHideDuration: null keeps the message on screen indefinitely
      notify(error.message, {type: "error", autoHideDuration: null, multiLine: true})
    })
  }

  React.useEffect(() => {
    if (!window?.google || !divRef.current) {
      return
    }

    window.google.accounts.id.initialize({
      ...gsiParams,
      callback: handleLogin,
    })

    window.google.accounts.id.renderButton(divRef.current, {
      width: "300px",
      ...props,
    })
    // we need to react on the presence of window.google
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [window?.google, gsiParams, login, props])

  return (
    <div
      ref={divRef}
      id="ra-google-login-button"
    />
  )
}

export const LoginButton = (props: LoginButtonProps) => {
  const {sx, ...rest} = props

  return (
    <StyledBox sx={sx}>
      <GoogleButton {...rest} />
    </StyledBox>
  )
}

const PREFIX = "RaGoogleLoginButton"

const StyledBox = styled(Box, {
  name: PREFIX,
  overridesResolver: (props, styles) => styles.root,
})(({theme}) => ({
  marginTop: theme.spacing(4),
}))

export interface LoginButtonProps extends GsiButtonConfiguration {
  sx?: SxProps
}
