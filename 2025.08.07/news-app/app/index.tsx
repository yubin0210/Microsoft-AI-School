import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";
import { Pressable, StyleSheet } from "react-native";
import { FlatList } from "@/components/ui/flat-list";
import { useEffect, useState } from "react";
import { Stack } from "expo-router";

interface NewsItemProps {
    title: string;
    link?: string;
    guid?: string;
    pubDate?: string;
    description?: string;
    source?: string;
    sourceUrl?: string;
}

export default function RootScreen() {
    const [news, setNews] = useState<NewsItemProps[]>([]);

    useEffect(() => {
        console.log("INITIALIZED ROOT SCREEN")
        requestNews();
        // fetch("http://localhost:8000/v1/news/", {
        //     method: "GET",
        // }).then((response) => {

        //     if (response.status == 200) {
        //         return response.json();
        //     } 
        // })
        // .then((response_json) => {
        //     console.log(response_json);
        //     setNews([{title: "테스트용 데이터"}])
        // })
        
    }, []);

    useEffect(() => {
        console.log("NEWS 데이터가 변경되었습니다.", news)
    }, [news]);

    const requestNews = async () => {

        const response = await fetch("http://localhost:8000/v1/news/", {
            method: "GET",
        });
        const response_json = await response.json()
        console.log(response_json)
        setNews(response_json.data);
    }

    const renderTitle = () => {
        return (
            <Box style={{ padding: 20, backgroundColor: 'lightblue' }}>
                <Text size="2xl" style={{ textAlign: 'center' }}>
                    FlastList Example
                </Text>
            </Box>
        )
    }


    const getItemView = (item: NewsItemProps) => {
    return (
        <Pressable
            style={styles.card}
            onPress={() => {
                if (item.link) {
                    console.log("뉴스 링크:", item.link);
                    // Linking.openURL(item.link);
                }
            }}
        >
            <Text size="xl" style={styles.title}>
                {item.title}
            </Text>

            {item.pubDate && (
                <Text size="sm" style={styles.date}>
                    {new Date(item.pubDate).toLocaleString()}
                </Text>
            )}

            {item.source && (
                <Text size="sm" style={styles.source}>
                    {item.source}
                </Text>
            )}
        </Pressable>
        );
    };
    
    const renderList = () => {
        return (
            <Box style={{flex: 1}}>
                <FlatList
                    data={news}
                    renderItem={({ item }) => getItemView(item)}
                    keyExtractor={(item, index) => index.toString()}
                />
            </Box>
        )
    }

    return (
        <Box style={{ flex: 1 }}>
            <Stack.Screen
                options={{
                    headerTitle: "뉴스",
                    headerStyle: { backgroundColor : "#5477d7ff"},
                    headerTitleStyle: { color: "#ffffffff"},
                }}
            />
            {renderList()}
        </Box>
    )
}

const styles = StyleSheet.create({
    card: {
        backgroundColor: 'white',
        borderRadius: 12,
        padding: 16,
        marginVertical: 8,
        marginHorizontal: 16,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.1,
        shadowRadius: 4,
        elevation: 3,
    },
    title: {
        fontWeight: 'bold',
        marginBottom: 6,
    },
    date: {
        color: '#888',
        marginBottom: 8,
    },
    description: {
        color: '#444',
    },
    source: {
        color: '#0066cc',
        marginTop: 8,
    },
    descriptionContainer: {
    marginBottom: 8,
    maxHeight: 60, // 높이 제한 (선택사항)
    overflow: 'hidden',
    },
});