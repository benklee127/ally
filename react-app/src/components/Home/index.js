import UserHome from "./UserHome";
import DefaultHome from "./DefaultHome";
import { useSelector } from "react-redux";

export default function Home() {

    const currentUser = useSelector((state) => state.session.user);

    if(currentUser) {
        return (
            <UserHome />
        )
    } else {
        return (
            <DefaultHome />
        )
    }
};