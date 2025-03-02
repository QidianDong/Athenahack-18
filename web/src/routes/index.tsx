// import ky from 'ky';
// function Index() {
//   return (
//     <div className="p-2">
//       <h3>Welcome Home!</h3>
//     </div>
//   );
// }

// export default Index;
import React, { useEffect } from 'react';
import ky from 'ky';

const Index: React.FC = () => {

  useEffect(() => {
    const getUrl = 'https://api.example.com/data';

    ky.get(getUrl)
      .json()
      .then((data) => {
        console.log('GET Request Successful!');
        console.log(data); 
      })
      .catch((error) => {
        console.error('GET Request Failed:', error);
      });
  }, []); 


  const handlePostRequest = async () => {
    const postUrl = 'https://api.example.com/submit';
    const postData = {
      key1: 'value1',
      key2: 'value2',
    };

    try {
      const responseData = await ky.post(postUrl, { json: postData }).json();
      console.log('POST Request Successful!');
      console.log(responseData);
    } catch (error) {
      console.error('POST Request Failed:', error);
    }
  };

  return (
    <div className="p-2">
      <h3>Welcome Home!</h3>
      <p>This is a sample page with GET and POST requests.</p>
      
      {}
      <button onClick={handlePostRequest} className="btn btn-primary">
        Send POST Request
      </button>
    </div>
  );
};

export default Index;

