import React from "react";
import "../style/CategoryCard.css"


function CategoryCard(props) {
    return( 
        <div className="category-card">
            <div className="category-text-card">
                <h4 >{props.category.category}</h4>
                <h4 >{props.category.amount}</h4>
            </div>
        </div>
        );
}

export default CategoryCard;
