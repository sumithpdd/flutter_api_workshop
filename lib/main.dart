import 'package:flutter/material.dart';
import 'package:flutter_api_workshop/data/local_json_books_repository.dart';
import 'package:flutter_api_workshop/data/books_repository.dart';
import 'package:flutter_api_workshop/presentation/books_page.dart';
import 'package:flutter/services.dart';
import 'dart:convert';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final booksJson = json.decode(
    await rootBundle.loadString('assets/data/books.json'),
  );
  // final booksDio = Dio(
  //     BaseOptions(
  //       baseUrl: 'https://www.googleapis.com/books/v1/',
  //     favesApiClient,
  //   );
  final localJsonBooksRepository = LocalJsonBooksRepository(booksJson);

  runApp(BooksApp(booksRepository: localJsonBooksRepository));
}

class BooksApp extends StatelessWidget {
  final BooksRepository booksRepository;

  const BooksApp({super.key, required this.booksRepository});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter API Demo',
      theme: ThemeData(primarySwatch: Colors.brown),
      home: BooksPage(booksRepository: booksRepository),
    );
  }
}
