import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";
import { router } from "expo-router";
import { Pressable } from "react-native";

export default function RootScreen() {

    const onItemClicked = () => {
        router.push("/sign-in");
    }
    return (
        <Box>
            <Pressable onPress={onItemClicked} style={{alignItems: 'center', padding: 20, backgroundColor: 'orange',
                borderRadius: 10, margin: 20
            }}>
                <Text style={{color: 'white'}}>로그인</Text>
            </Pressable>
        </Box>
    )
}