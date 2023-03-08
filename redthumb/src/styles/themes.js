import { Colors } from "./colors";

export const palette = {
    primary: {
        main: Colors.primary,
        dark: Colors.primary_dark,
    },
    secondary: {
        main: Colors.secondary,
    },
};

const appTheme = {
    components: {
        MuiAppBar: {
            styleOverrides: {
                root: {
                    boxShadow: "none",
                },
            },
        },
    },
    shape: {
        searchbar: {
            borderRadius: 50,
        },
    },
};

export default appTheme;