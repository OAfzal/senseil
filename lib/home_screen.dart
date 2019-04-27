import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final myController = TextEditingController();

  var controllerArray = [];

  @override
  void dispose() {
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomPadding: true,
      appBar: AppBar(
        centerTitle: true,
        title: Text(
          "Data Input",
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 25.0),
        ),
        backgroundColor: Color(0xffea9504),
      ),
      body: SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[getTextCard("PH"), getTextCard("Ca")],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[getTextCard("P"), getTextCard("C")],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[getTextCard("Sand")],
            ),
            RaisedButton(
              // padding: EdgeInsets.symmetric(horizontal: 15.0),
              color: Color(0xffea9504),
              shape: new RoundedRectangleBorder(
                  borderRadius: new BorderRadius.circular(10.0)),
              child: Text(
                "Submit",
                style: TextStyle(color: Colors.white, fontSize: 20.0),
              ),
              onPressed: () {
                getData();
              },
            )
          ],
        ),
      ),
    );
  }

  getTextCard(label) {
    controllerArray.add(TextEditingController());
    return Container(
      margin: EdgeInsets.all(15.0),
      width: 65.0,
      child: TextField(
        // textInputAction: TextInputAction.next,
        controller: controllerArray[controllerArray.length - 1],
        keyboardType: TextInputType.numberWithOptions(),
        autofocus: true,
        maxLength: 4,
        decoration: InputDecoration(
            border: OutlineInputBorder(), labelText: label, counterText: ""),
      ),
    );
    // Row(
    //   children: <Widget>[
    //     Text(
    //       label,
    //       style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20.0),
    //     ),

    //   ],
    // );
  }

  getData() {
    print("here");
    String text = "";
    var arr = [];
    for (int i = 0; i < controllerArray.length; i++) {
      // print(controllerArray[i].text);
      arr.add(controllerArray[i].text);
    }
    sendData(arr);
  }

  sendData(arr) async {
    var baseURL = "http://192.168.1.128:5000/predicted?";
    baseURL += "ph=" + arr[0];
    baseURL += "&ca=" + arr[1];

    baseURL += "&p=" + arr[2];
    baseURL += "&sol=" + arr[3];
    baseURL += "&sand=" + arr[4];
    print(baseURL);
    var response = await http.get(baseURL);
    print(response.body);
    _showDialog(response.body);
  }

  void _showDialog(results) {
    // flutter defined function
    showDialog(
      context: context,
      builder: (BuildContext context) {
        // return object of type Dialog
        return AlertDialog(
          title: new Text("Result"),
          content: new Text(results),
          actions: <Widget>[
            // usually buttons at the bottom of the dialog
            new FlatButton(
              child: new Text("Close"),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }
}
