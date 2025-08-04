import { Box } from "@/components/ui/box";
import { Button, ButtonText } from "@/components/ui/button";
import { Divider } from "@/components/ui/divider";
import { Input, InputField } from "@/components/ui/input";
import { Text } from "@/components/ui/text"
import { useState } from "react";


export default function SignInScreen() {

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("");

    const onSignInClicked = () => {
        console.log(username, password);
        console.log("로그인 버튼 클릭");
    }
    
    return (
    <Box style={{padding: 20}}>
        <Box style={{padding: 50}}>
            <Text>로그인 하세요 !!</Text>
        </Box>
        <Input
            variant="rounded"
            size="md"
            style={{marginBottom: 20}}
        >
            <InputField placeholder="아이디를 입력하세요." defaultValue={username} onChangeText={(text) => {
                setUsername(text);
            }}/>
        </Input>
        <Input
            variant="rounded"
            size="md"
        >
            <InputField placeholder="패스워드를 입력하세요." defaultValue={password} onChangeText={(text) => {
                setPassword(text);
            }}/>
        </Input>
        <Divider style={{marginVertical: 20}}/>
        <Button variant="outline" onPress={onSignInClicked}>
            <ButtonText>로그인</ButtonText>
        </Button>
    </Box>
    )
}