import 'package:flutter/material.dart';
import 'package:flutter_api_workshop/common/app_theme.dart';

class BookListItemCover extends StatelessWidget {
  final String imageUrl;

  const BookListItemCover({super.key, required this.imageUrl});

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: const BorderRadius.all(Radius.circular(12)),
      child: Image.network(
        imageUrl,
        width: 84,
        height: 92,
        fit: BoxFit.cover,
        errorBuilder: (_, __, ___) {
          return Container(
            width: 84,
            height: 92,
            color: AppTheme.accentColorLight,
          );
        },
      ),
    );
  }
}
