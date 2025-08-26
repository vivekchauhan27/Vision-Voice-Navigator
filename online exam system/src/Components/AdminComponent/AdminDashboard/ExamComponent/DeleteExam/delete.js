async function deleteExam(id) {
    try {
        console.log("Fetching all questions...");
        let value = await axios.get("http://localhost:3333/question");
        setQuestions(value.data);
        console.log("Questions fetched:", questions);

        console.log("Deleting questions related to exam:", id);
        for (let i = 0; i < questions.length; i++) {
            if (parseInt(questions[i].exam_id) === parseInt(id)) {
                console.log("Deleting question with id:", questions[i].id);
                await axios.delete(`http://localhost:3333/question/${questions[i].id}`);
            }
        }

        console.log("Deleted questions. Now deleting the exam:", id);
        await axios.delete(`http://localhost:3333/exam/${id}`);
        setStatusDeleteExam(true);

        console.log("Exam deleted successfully.");
    } catch (error) {
        console.error("Error deleting exam:", error);
    }
}
