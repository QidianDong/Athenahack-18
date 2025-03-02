import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea"
import ky from 'ky';
import { useEffect } from "react";
import { GlobalNavbar } from "../components/globalnav";


function Index() {

  async function sendToServer() {
    const url = "https://api.example.com";

    return await ky.get(url).json().catch((error: any) => { console.error("Request Failed", error) })

  }

  useEffect(() => {
    const getUrl = 'https://api.example.com/data';
  
    ky.get(getUrl)
      .json()
      .catch((error: any) => {
        console.error('GET Request Failed:', error);
      });
  });

  return (
    <>
    <section className="bg-[url(assets/mesh-gradient.png)] bg-center bg-auto h-screen backdrop-opacity-90 backdrop-blur-md">
    <GlobalNavbar />


    <h1 className="mt-16 scroll-m-20 text-4xl font-extrabold tracking-normal lg:text-5xl text-center">
      Insert Gene
    </h1>
    <h3 className="mt-4 scroll-m-2 text-1xl font-extrabold tracking-normal lg:text-3xl text-center">
      yooo
    </h3>
    <div className="py-8 grid  h-3xl w-2xl gap-2  justify-self-center">
      <Textarea placeholder="Type or copy and paste your content here" />
      <Button onClick={sendToServer}>Analyze!</Button>
      </div>
    </section>
    </>
  )
};
export default Index;
