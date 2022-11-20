import React,{ useState,useEffect } from "react";
import axios from "axios"
import CategoryCard from "./CategoryCard"
import "../style/Breakdown.css"
import consts from "../model/Consts";


function Breakdown() {
    const [breakdown, setBreakdown] = useState([]);
    useEffect(()=>{
        axios.get(consts.CATEGORIES_BREAKDOWN_URL).then(res=>{setBreakdown(res.data)})
    },[])
    return <div className="breakdown">{breakdown.map((c,i)=><CategoryCard key={i} category={c}/>)}</div>;
}

export default Breakdown;
