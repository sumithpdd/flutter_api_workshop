// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:flutter_api_workshop/main.dart';
import 'package:flutter_api_workshop/data/in_memory_books_repository.dart';

void main() {
  testWidgets('Books app smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(
      BooksApp(booksRepository: InMemoryBooksRepository()),
    );

    // Verify that the app loads with the correct title
    expect(find.text('Books Search'), findsOneWidget);
    expect(find.text('Start book search...'), findsOneWidget);

    // Verify that the search bar is present
    expect(find.byType(TextFormField), findsOneWidget);

    // Verify that the floating action button for favorites is present
    expect(find.byIcon(Icons.favorite_sharp), findsOneWidget);

    // Wait for the books to load
    await tester.pumpAndSettle();

    // Verify that books are displayed (InMemoryBooksRepository has one book)
    expect(find.text('Marina'), findsOneWidget);
    expect(find.text('Carlos Ruiz Zafon'), findsOneWidget);
  });
}
