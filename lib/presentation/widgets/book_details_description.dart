import 'package:flutter/material.dart';
import 'package:flutter_api_workshop/common/app_theme.dart';
import 'package:flutter_html/flutter_html.dart';

class BookDetailsDescription extends StatelessWidget {
  final String description;

  const BookDetailsDescription({super.key, required this.description});

  @override
  Widget build(BuildContext context) {
    final bodyStyle = Style(
      color: AppTheme.grayDark,
      fontFamily: AppTheme.accentFontFamily,
      fontWeight: FontWeight.w400,
      fontSize: FontSize(16),
    );

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const SizedBox(height: 16),
        const Padding(
          padding: EdgeInsets.symmetric(horizontal: 16),
          child: Text(
            'Description',
            style: TextStyle(
              color: AppTheme.grayDark,
              fontFamily: AppTheme.primaryFontFamily,
              fontWeight: FontWeight.w700,
              fontSize: 20,
            ),
          ),
        ),
        Container(
          margin: const EdgeInsets.only(left: 8, right: 8),
          child: Html(
            data: description,
            style: {'body': bodyStyle, 'b': bodyStyle},
          ),
        ),
      ],
    );
  }
}
