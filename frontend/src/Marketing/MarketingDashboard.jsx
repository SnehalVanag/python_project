import React, { useState } from 'react';
// import PromotionList from './PromotionList';
// import LeadsCounter from './LeadsCounter';
// import AddPromotionForm from './AddPromotionForm';
import './MarketingDashboard.css';

const MarketingDashboard = () => {
  const [promotions, setPromotions] = useState([]);
//   const [showAddForm, setShowAddForm] = useState(false);

//   const handleAddPromotion = (newPromotion) => {
//     setPromotions([...promotions, { ...newPromotion, id: Date.now() }]);
//     setShowAddForm(false);
//   };

//   const handleDeletePromotion = (id) => {
//     setPromotions(promotions.filter(promo => promo.id !== id));
//   };

  return (
    <div className="dashboard-container">
      <h1>Marketing Team Dashboard</h1>
      
      <div className="dashboard-stats">
        {/* <LeadsCounter /> */}
      </div>

      <div className="dashboard-actions">
        <button 
          className="add-button"
          onClick={() => setShowAddForm(true)}
        >
          Add New Promotion
        </button>
      </div>

      {/* <PromotionList 
        promotions={promotions} 
        onDelete={handleDeletePromotion} 
      /> */}

      {/* {showAddForm && (
        <AddPromotionForm 
          onAdd={handleAddPromotion}
          onClose={() => setShowAddForm(false)}
        />
      )} */}
    </div>
  );
};

export default MarketingDashboard;