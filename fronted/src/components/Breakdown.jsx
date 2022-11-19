import React,{ useState,useEffect } from "react";
import axios from "axios"
import CategoryCard from "./CategoryCard"
import "../style/Breakdown.css"


function Breakdown() {
    const [breakdown, setBreakdown] = useState([]);
    useEffect(()=>{
        axios.get('http://localhost:8080/categories/breakdown').then(res=>{setBreakdown(res.data)})
    },[])
    console.log(breakdown)
    return <div className="breakdown">{breakdown.map((c,i)=><CategoryCard key={i} category={c}/>)}</div>;
}

export default Breakdown;
