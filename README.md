# Flutter Books API Workshop

A comprehensive Flutter application demonstrating modern app architecture, API integration, and state management for a book search and favorites system.

## 📱 App Overview

This Flutter app allows users to:
- **Search for books** using the Google Books API
- **View book details** including cover images, descriptions, ratings, and metadata
- **Add/remove books to favorites** with persistent storage
- **Browse favorite books** in a dedicated section
- **Responsive UI** with modern Material Design

## 🏗️ Architecture

The app follows **Clean Architecture** principles with clear separation of concerns:

```
lib/
├── data/           # Data layer (repositories, API clients, models)
├── presentation/   # UI layer (pages, widgets)
│   └── widgets/    # Reusable UI components
├── common/         # Shared components (theme, utilities)
└── main.dart       # App entry point
```

### Architecture Pattern: Repository Pattern

The app uses the **Repository Pattern** to abstract data sources:

- **`BooksRepository`** - Abstract interface defining book operations
- **`LocalJsonBooksRepository`** - Reads from local JSON file (for development/testing)
- **`NetworkBooksRepository`** - Fetches from Google Books API (production)
- **`InMemoryBooksRepository`** - In-memory storage (for testing)

## 📦 Dependencies & Why They're Used

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `dio` | ^5.8.0+1 | **HTTP client** for API calls with interceptors, request/response transformation |
| `json_annotation` | ^4.9.0 | **JSON serialization** annotations for automatic code generation |
| `equatable` | ^2.0.7 | **Value equality** for comparing objects without manual implementation |
| `flutter_html` | ^3.0.0 | **HTML rendering** for rich text descriptions from API |

## 🔌 API Integration

### Google Books API

The app integrates with the **Google Books API** for fetching book data:

- **Base URL**: `https://www.googleapis.com/books/v1/`
- **Search Endpoint**: `GET /volumes?q={search_terms}&maxResults=40`
- **Book Details**: `GET /volumes/{volume_id}`

#### API Features Used:
- **Search by title, author, ISBN**: `q=harry+potter+rowling`
- **Filter by type**: `q=subject:fiction`
- **Limit results**: `maxResults=40`
- **Pagination**: `startIndex=0`

#### Response Structure:
```json
{
  "kind": "books#volumes",
  "totalItems": 1234,
  "items": [
    {
      "kind": "books#volume",
      "id": "volume_id",
      "volumeInfo": {
        "title": "Book Title",
        "authors": ["Author Name"],
        "description": "Book description...",
        "imageLinks": {
          "thumbnail": "cover_url"
        }
      }
    }
  ]
}
```

### Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `build_runner` | ^2.4.13 | **Code generation** tool for JSON serialization |
| `json_serializable` | ^6.8.0 | **JSON code generation** creates `.fromJson()` and `.toJson()` methods |
| `flutter_lints` | ^5.0.0 | **Code quality** rules and best practices enforcement |
| `flutter_launcher_icons` | ^0.13.1 | **App icon generation** for all platforms |

## 🚀 Getting Started

### Prerequisites

- **Flutter SDK** (3.8.1 or higher)
- **Dart SDK** (3.8.1 or higher)
- **Android Studio** / **VS Code** with Flutter extensions
- **Git** for version control

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/your-username/flutter_api_workshop.git

# Navigate to project directory
cd flutter_api_workshop
```

#### 2. Install Dependencies

```bash
# Get all dependencies
flutter pub get

# Generate JSON serialization code
dart run build_runner build
```

#### 3. Run the App

```bash
# Run on connected device/emulator
flutter run

# Or run in debug mode
flutter run --debug

# Or run in release mode
flutter run --release
```

#### 4. Run Tests

```bash
# Run all tests
flutter test

# Run tests with coverage
flutter test --coverage
```

#### 5. Generate App Icons

```bash
# Generate launcher icons for all platforms
flutter pub run flutter_launcher_icons:main
```

**Note**: See `setup_icons_and_splash.md` for detailed instructions on creating the custom app icon.

## 📁 Project Structure Deep Dive

### Data Layer (`lib/data/`)

#### Core Models
- **`book.dart`** - Main Book entity with business logic
- **`book_response.dart`** - API response models with JSON annotations
- **`fave_book_response.dart`** - Favorite book API models

#### Repository Implementations
- **`books_repository.dart`** - Abstract interface
- **`local_json_books_repository.dart`** - Local JSON file implementation
- **`network_books_repository.dart`** - Google Books API implementation
- **`in_memory_books_repository.dart`** - In-memory implementation for testing

#### API Clients
- **`books_api_client.dart`** - Google Books API client using Dio
- **`faves_api_client.dart`** - Favorites API client for CRUD operations

### Presentation Layer (`lib/presentation/`)

#### Pages
- **`books_page.dart`** - Main search and list page
- **`book_details_page.dart`** - Individual book details view
- **`fave_books_page.dart`** - Favorites list page

#### Widgets (`lib/presentation/widgets/`)
- **`book_list_item.dart`** - Book list item component
- **`book_list_item_cover.dart`** - Book cover image widget
- **`book_list_item_info.dart`** - Book information display widget
- **`book_list_item_rating.dart`** - Book rating stars widget
- **`book_details_cover_image.dart`** - Large book cover image for details
- **`book_details_main_info.dart`** - Book title, subtitle, and author info
- **`book_details_description.dart`** - Book description with HTML rendering
- **`book_details_numbers_segment.dart`** - Book metadata display (pages, rating, year)
- **`book_details_number_segment_item.dart`** - Individual metadata item widget

### Common Layer (`lib/common/`)

- **`app_theme.dart`** - App-wide theme configuration
- **`search_bar.dart`** - Reusable search input component
- **`sliver_search_app_bar.dart`** - Sliver-based search header (legacy)

### Assets (`assets/`)

- **`icons/`** - App launcher icons and icon resources
  - **`app_icon.svg`** - Source SVG icon (person reading a book)
  - **`app_icon.png`** - Generated PNG icon (1024x1024)
  - **`icon_description.md`** - Icon design specifications
- **`fonts/`** - Custom font files (KohSantepheap, Inter)
- **`data/`** - Local JSON data files

## 🔄 Switching Between Repositories

The app supports multiple data sources. Here's how to switch:

### 1. Local JSON Repository (Default)

```dart
// In main.dart - already configured
final booksJson = json.decode(
  await rootBundle.loadString('assets/data/books.json'),
);
final localJsonBooksRepository = LocalJsonBooksRepository(booksJson);
```

**Use case**: Development, testing, offline demo

### 2. Network Repository (Google Books API)

```dart
// In main.dart - uncomment and configure
final booksDio = Dio(
  BaseOptions(
    baseUrl: 'https://www.googleapis.com/books/v1/',
    // Optional: Add API key for higher rate limits
    // queryParameters: {'key': 'YOUR_API_KEY'},
  ),
);
final favesDio = Dio(
  BaseOptions(
    baseUrl: 'https://your-faves-api.com/',
  ),
);

final booksApiClient = BooksApiClient(booksDio);
final favesApiClient = FavesApiClient(favesDio);
final networkBooksRepository = NetworkBooksRepository(booksApiClient, favesApiClient);
```

**Use case**: Production app with real API data

#### Google Books API Configuration

The Google Books API is **free to use** with the following limits:
- **1,000 requests per day** (without API key)
- **100,000 requests per day** (with API key)

To get an API key:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable the "Books API" service
4. Create credentials (API key)
5. Add the key to your Dio configuration

**Note**: The API works without authentication for basic usage, but an API key is recommended for production apps.

### 3. In-Memory Repository (Testing)

```dart
// In test files
final inMemoryRepository = InMemoryBooksRepository();
```

**Use case**: Unit tests, widget tests

## 🛠️ Development Workflow

### Adding New Features

1. **Create/Update Models** in `lib/data/`
2. **Generate JSON code**: `dart run build_runner build`
3. **Update Repository** interface and implementations
4. **Create UI Components** in `lib/presentation/`
5. **Write Tests** in `test/` directory

### Code Generation

```bash
# Generate JSON serialization code
dart run build_runner build

# Watch for changes and auto-generate
dart run build_runner watch

# Clean generated files
dart run build_runner clean

# Force rebuild
dart run build_runner build --delete-conflicting-outputs
```

### Adding New API Endpoints

1. **Update API Client** (`books_api_client.dart` or `faves_api_client.dart`)
2. **Create Response Models** with JSON annotations
3. **Generate Code**: `dart run build_runner build`
4. **Update Repository** implementation
5. **Add UI Components**

## 🧪 Testing

### Widget Tests

```bash
# Run widget tests
flutter test test/widget_test.dart

# Run with coverage
flutter test --coverage
```

### Repository Testing

```dart
// Example test structure
void main() {
  group('BooksRepository Tests', () {
    late InMemoryBooksRepository repository;

    setUp(() {
      repository = InMemoryBooksRepository();
    });

    test('should return books list', () async {
      final books = await repository.getBooks();
      expect(books, isNotEmpty);
    });
  });
}
```

## 🎨 Customization

### Theme Customization

Edit `lib/common/app_theme.dart`:

```dart
class AppTheme {
  static const Color primaryColor = Color(0xFFF5E6D3);
  static const Color accentColor = Color(0xFF8B4513);
  // ... customize colors, fonts, etc.
}
```

### Adding New Fonts

1. Add font files to `assets/fonts/`
2. Update `pubspec.yaml`:

```yaml
fonts:
  - family: YourFont
    fonts:
      - asset: assets/fonts/YourFont-Regular.ttf
        weight: 400
```

### Customizing App Icon

1. **Replace the icon**: Update `assets/icons/app_icon.png` with your custom 1024x1024 PNG
2. **Regenerate icons**: Run `flutter pub run flutter_launcher_icons:main`
3. **Customize colors**: Update the `flutter_launcher_icons` configuration in `pubspec.yaml`

#### Icon Requirements:
- **Size**: 1024x1024 pixels
- **Format**: PNG with transparency support
- **Style**: Modern, clean, recognizable at small sizes
- **Theme**: Should match your app's color scheme

## 🚀 Deployment

### Android

```bash
# Build APK
flutter build apk --release

# Build App Bundle
flutter build appbundle --release
```

### iOS

```bash
# Build for iOS
flutter build ios --release
```

## 🔧 Troubleshooting

### Common Issues

1. **JSON Generation Errors**
   ```bash
   dart run build_runner clean
   dart run build_runner build --delete-conflicting-outputs
   ```

2. **Dependency Issues**
   ```bash
   flutter clean
   flutter pub get
   ```

3. **API Connection Issues**
    - Check internet connection
    - Verify API endpoints in API clients
    - Check API keys if required

4. **Icon Generation Issues**
    ```bash
    # Clean and regenerate icons
    flutter clean
    flutter pub get
    flutter pub run flutter_launcher_icons:main
    ```
    - Ensure `assets/icons/app_icon.png` exists and is 1024x1024 pixels
    - Check that `flutter_launcher_icons` is in dev_dependencies

### Debug Mode

```bash
# Run with verbose logging
flutter run --verbose

# Check Flutter doctor
flutter doctor
```

## 📚 Learning Resources

- [Flutter Documentation](https://flutter.dev/docs)
- [Dio HTTP Client](https://pub.dev/packages/dio)
- [JSON Serialization](https://pub.dev/packages/json_annotation)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `flutter test`
5. Commit changes: `git commit -m 'Add feature'`
6. Push to branch: `git push origin feature-name`
7. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the Flutter documentation

---

**Happy Coding! 📚✨**
